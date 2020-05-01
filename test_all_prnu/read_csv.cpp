#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    char * buffer = NULL;
    char * piece = NULL;
    size_t len = 0;
    size_t max_len = 0;
    int i = 0;
    string file_name = "data.csv";
    vector<vector<string> > content_list;
    FILE *file = fopen(file_name.c_str(), "r");

    while (getline(&buffer, &len, file) != -1) {
        vector<string> tmp;
        piece = strtok(buffer, ",");
        while (piece != NULL) {
            tmp.push_back(piece);
            piece = strtok(NULL, ",");
        }
        content_list.push_back(tmp);
        i++;
    }
    free(buffer);
    fclose(file);

    for (int i = 0; i < content_list.size(); i++) {
        for (int j = 0; j < content_list[i].size(); j++) {
            cout << content_list[i][j] << " "; 
        }
        cout << "\n";
    }

    return 0;
}
