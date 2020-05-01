#include<iostream>
#include<string>
#include<fstream>
constexpr auto TIMELINE_BEGIN = 13;
constexpr auto BASE = 50;
constexpr auto MAX_STRLEN = 100;

using namespace std;


string Get_ExifTime(string fileName)
{
	string ExifTime = "E:\\PRNU\\test_all\\2_51_1568772478_049_00_452620.jpg";

	fstream fin(fileName.c_str(), ifstream::in | ifstream::binary);
	if (!fin)
	{
		cerr << "error in open the JPG FILE" << endl;
		exit(-1);
	}

	int offset = 0;
	char str[MAX_STRLEN];
	memset(str, 0, sizeof(str));

	offset = TIMELINE_BEGIN * BASE + 4;
	fin.seekg(offset, ifstream::beg);
	fin.read(str, 19);
	ExifTime = str;

	fin.close();
	return ExifTime;
}