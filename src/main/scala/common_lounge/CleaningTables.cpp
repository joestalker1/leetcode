#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int clients[400];

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int m;
        int n;
        set<int> tables;
        map<int,vector<int>> client_to_pos;
        scanf("%d", &n);//table number
        scanf("%d", &m);//client number

        for (int i = 0; i < m; i++) {
            scanf("%d", &clients[i]);
            int clnt =  clients[i];
            if(client_to_pos.count(clnt) == 0){
                auto* ptr = new vector<int>();
                client_to_pos[clnt] = *ptr;
            }
            client_to_pos[clnt].push_back(i);
        }
        int clean = 0;
        for (int i = 0; i < m; i++) {
            int client = clients[i];
            client_to_pos[client].erase(client_to_pos[client].begin());
            //check if client is on the table
            if (tables.count(client) > 0) {
                continue;
            } else if (tables.size() < n) {
                tables.insert(client);
                clean += 1;
            } else {
                //evict client with order equals 0
                int appropriate_client = -1;
                int max_dist = 0;
                for (auto clnt : tables) {
                    if(client_to_pos[clnt].size() == 0){
                        appropriate_client = clnt;
                        break;
                    }
                    if(client_to_pos[clnt][0] > max_dist){
                        max_dist = client_to_pos[clnt][0];
                        appropriate_client = clnt;
                    }
                }
                tables.erase(appropriate_client);
                tables.insert(client);
                clean += 1;
            }
        }
        printf("%d\n", clean);
    }
    return 0;
};
