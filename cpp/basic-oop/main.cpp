#include <iostream>
#include <string>
#include "cameraClass.cpp"
using namespace std;


int main()
{
    Camera canon("Canon", 4096, 450, "4000D", 8.25, 5, true);
    Camera nikon("Nikon", 8192, 580, "D3500", 5.75, 5, true);
    Camera polaroid("Polaroid", 0, 320, "635CL", 2.0, 2, false);
    Camera * cameras[3] = {&canon, &nikon, &polaroid}; // array of objects

    for (int i=0; i<3; i++)
    {
        cout << "Information about camera #" << i+1 << ": " << endl;
        cout << "Manufacturer: " << cameras[i]->getManufacturer() << endl;
        cout << "Model: " << cameras[i]->getModel() << endl;
        cout << "Price: $" << cameras[i]->getPrice() << endl;
        cout << "Zoom level: " << cameras[i]->getZoom() << endl;
        cout << "Storage (MiB): " << cameras[i]->getStorage() << endl;
        cout << "Warranty (years): " << cameras[i]->getWarranty() << endl;
        cout << "Flash availability: " << convert(cameras[i]->getFlash()) << endl;
        cout << "-----------" << endl;
    }
    return 0;
}

string convert(bool exp)
{
    if (exp) return "yes";
    else return "no";
}
