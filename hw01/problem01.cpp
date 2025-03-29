#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <cmath>



struct point{
    double x;
    double y;
    double z;
    char c;
};

std::ostream& operator<<(std::ostream& os,const point& p){
    os<<p.x<<' '<<p.y<<' '<<p.z<<' '<<p.c;
    return os;
}

const point BASE={8,9,111,'1'};

const double calcDist(const point& p){
    return std::sqrt((BASE.x-p.x)*(BASE.x-p.x)+(BASE.y-p.y)*(BASE.y-p.y)+(BASE.z-p.z)*(BASE.z-p.z));
}

struct compare{
    bool operator()(const point& lp,const point& rp){
        return calcDist(lp)>calcDist(rp);
    }
};

std::unordered_map<char,double> m;

int main(){

    std::vector<point> v;
    v.push_back({7,8,200,'a'});
    v.push_back({8,9,220,'a'});
    v.push_back({6,6,180,'a'});
    v.push_back({7.5,8.5,210,'a'});
    v.push_back({6.5,7,190,'a'});

    v.push_back({5,5,100,'b'});
    v.push_back({5.5,4.5,120,'b'});
    v.push_back({6,5,130,'b'});
    v.push_back({5,6,110,'b'});
    v.push_back({5.5,5,115,'b'});

    v.push_back({2,2,50,'c'});
    v.push_back({2.5,2.5,55,'c'});
    v.push_back({1.5,2,45,'c'});
    v.push_back({2,2.5,53,'c'});
    v.push_back({3,2,58,'c'});

    v.push_back({10,3,120,'d'});
    v.push_back({12,3.1,110,'d'});
    v.push_back({11,2.9,130,'d'});
    v.push_back({14,3,120,'d'});
    v.push_back({15,2.6,110,'d'});

    std::priority_queue<point,std::vector<point>,compare> pq(v.begin(),v.end());


    for(int i=0;i<5;++i){
        const point now(pq.top());
        pq.pop();

        const double value=exp(-calcDist(now));
        std::cout<<now<<" value : "<<value<<'\n';
        
    
        m[now.c]+=value;
    }

    for(auto i=m.begin();i!=m.end();++i){
        std::cout<<i->first<<" : "<<i->second<<'\n';
    }

    return 0;
}