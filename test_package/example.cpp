#include <iostream>

#include <matroska/KaxVersion.h>

int main(int argc, const char* argv[])
{
    const std::string expected = "1.6.3";

    if (libmatroska::KaxCodeVersion != expected) {
        std::cerr << "Invalid KaxCodeVersion (expected '" << expected << "' got '" << libmatroska::KaxCodeVersion << "')" << std::endl;
        return -1;
    }
}
