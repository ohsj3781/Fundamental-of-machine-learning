#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <cmath>

const int N=3;

struct Node{
    int id;
    int a;
    int b;
    int c;
    int d;
    int price;
};

std::ostream& operator<<(std::ostream& out, const Node& node) {
    out <<"id: "<<node.id<<" : "<< node.a << " " << node.b << " " << node.c << " " << node.d << " " << node.price;
    return out;
}

const Node BASE={-1,6,200,5,30,-1};

const double calcL2Distance(const Node& n) {
    return std::sqrt((n.a - BASE.a) * (n.a - BASE.a) +
                     (n.b - BASE.b) * (n.b - BASE.b) +
                     (n.c - BASE.c) * (n.c - BASE.c) +
                     (n.d - BASE.d) * (n.d - BASE.d));
}


struct Compare {
    bool operator()(const Node& n1, const Node& n2) {
        return calcL2Distance(n1) > calcL2Distance(n2);
    }
};



int main(){
    std::vector<Node> v;
    v.push_back({1,2,200,4,27,30000});
    v.push_back({2,5,150,3,35,20000});
    v.push_back({3,3,180,4,25,25000});
    v.push_back({4,1,230,2,10,21000});
    v.push_back({5,5,180,5,40,38000});
    v.push_back({6,4,210,3,30,31000});


    std::priority_queue<Node,std::vector<Node>,Compare> pq(v.begin(),v.end());

    double price=0;
    double weight=0;

    for(int i=0;i<5;++i){
        const Node now(pq.top());
        pq.pop();

        std::cout<<now<<'\n';
        const double tempWeight=exp(-calcL2Distance(now));
        std::cout<<"tempWeight : "<<tempWeight<<'\n';
        price+=tempWeight*now.price;
        weight+=tempWeight;
    }

    std::cout<<"price : "<<price/weight<<'\n';
}