#include <iostream>
#include <cmath>
#include <ctime>
#include <vector>
#include <stack>
#include <cstdlib>
#include <random>
#include <fstream>
#include <algorithm>

using namespace std;

struct Cell
{
    int x, y;
    char type;

    Cell(int x, int y, char type) : x(x), y(y), type(type) {}
};

class Maze
{
public:
    Maze(int width, int height) : width(width), height(height), generator(random_device{}())
    {
        grid = vector<vector<Cell>>(height, vector<Cell>(width, Cell(0, 0, '#')));
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                grid[i][j] = Cell(j, i, '#');
            }
        }
        generateMaze();
        establishStartFinish();
    }

    void printMaze()
    {
        for (const auto &row : grid)
        {
            for (const auto &cell : row)
            {
                cout << cell.type;
            }
            cout << '\n';
        }
    }

    void saveMazeToFile(const string &fname)
    {
        ofstream File(fname);
        if (!File)
        {
            cerr << "Error opening file" << fname << "\n";
            return;
        }

        File << height << '\n';
        File << width << '\n';

        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                char charType = grid[i][j].type;
                if (charType == '#')
                {
                    charType = 'w';
                }
                else if (charType == ' ')
                {
                    charType = 'p';
                }
                File << grid[i][j].x << ' ' << grid[i][j].y << ' ' << charType << '\n';
            }
        }
        File.close();
        cout << "Data saved" << endl;
    }

private:
    vector<vector<Cell>> grid;
    int width, height;
    Cell *start = nullptr;
    Cell *end = nullptr;
    default_random_engine generator;

    void generateMaze()
    {
        stack<Cell *> stack;

        grid[1][1].type = ' ';
        stack.push(&grid[1][1]);

        while (!stack.empty())
        {
            Cell *curr = stack.top();
            vector<Cell *> neighbor = getNeighbor(curr);
            if (!neighbor.empty())
            {
                uniform_int_distribution<int> dist(0, neighbor.size() - 1);
                Cell *next = neighbor[dist(generator)];
                destroyWall(curr, next);
                next->type = ' ';
                stack.push(next);
            }
            else
            {
                stack.pop();
            }
        }
    }

    vector<Cell *> getNeighbor(Cell *cell)
    {
        vector<Cell *> neighbor;
        static const int direction[4][2] = {{0, -2}, {-2, 0}, {0, 2}, {2, 0}};

        vector<int> order = {0, 1, 2, 3};
        shuffle(order.begin(), order.end(), generator);

        for (int i : order)
        {
            int newX = cell->x + direction[i][0];
            int newY = cell->y + direction[i][1];

            if (newX > 0 && newX < width - 1 && newY > 0 && newY < height - 1 && grid[newY][newX].type == '#')
            {
                neighbor.push_back(&grid[newY][newX]);
            }
        }
        return neighbor;
    }

    void establishStartFinish()
    {
        start = &grid[1][1];
        start->type = 's';

        end = &grid[height - 2][width - 2];
        end->type = 'e';
    }

    void destroyWall(Cell *a, Cell *b)
    {
        int Xwall = (a->x + b->x) / 2;
        int Ywall = (a->y + b->y) / 2;

        grid[Ywall][Xwall].type = ' ';
    }
};

void readSizeFromFile(const string &filename, int *width, int *height)
{
    ifstream file(filename);
    if (!file)
    {
        throw runtime_error("Error opening file " + filename);
    }

    if (!(file >> *width >> *height))
    {
        throw runtime_error("Error reading size data from file " + filename);
    }

    if (*width <= 0 || *height <= 0)
    {
        throw invalid_argument("Width and height must be positive integers");
    }

    file.close();
}

int main()
{
    int width;
    int height;
    readSizeFromFile("../app_file/maze_config.txt", &width, &height);
    Maze maze(width, height);
    maze.saveMazeToFile("../app_file/maze_map.txt");
    return 0;
}
