#include <iostream>
#include <string>
using namespace std;


class Camera
{
private:
    double zoom;
    int storage;
    string manufacturer;
protected:
    int warranty;
    bool flash;
public:
    Camera();
    ~Camera();
    Camera(string, int, int, string, double, int, bool);
    int price;
    string model;
    double getZoom();
    string getModel();
    string getManufacturer();
    int getPrice();
    int getStorage();
    int getWarranty();
    bool getFlash();
};

string convert(bool);