/*
 * @Description: 运行
./pcd2bin /home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.pcd /home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.bin
./pcd2bin /home/hcq/pointcloud/Python/data_process/data/000012.pcd /home/hcq/pointcloud/Python/data_process/data/000012.bin
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2021-07-30 17:13:40
 * @LastEditTime: 2021-08-16 16:33:01
 * @FilePath: /Python/data_process/pcdbin/pcd2bin/pcd2bin.cpp
 */
/*
 * @Author: your name
 * @Date: 2021-07-30 17:13:40
 * @LastEditTime: 2021-07-31 12:03:26
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /Python/data_process/pcdbin/pcd2bin.cpp
 */
#include <omp.h>
#include <ctime>
#include <vector>
#include <string>
#include <algorithm>

#include <pcl/io/pcd_io.h>
#include <pcl/common/common_headers.h>

#include <sys/stat.h>

#include <pcl/io/boost.h>
#include <boost/program_options.hpp>

#include <fstream>



void convertPCDtoBin(std::string &in_file, std::string& out_file)
{
	pcl::PointCloud<pcl::PointXYZI>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZI>);

	if (pcl::io::loadPCDFile<pcl::PointXYZI>(in_file, *cloud) == -1) //* load the file
	{
		std::string err = "Couldn't read file " + in_file;
		PCL_ERROR(err.c_str());
		return;// (-1);
	}
	std::cout << "Loaded "
		<< cloud->width * cloud->height
		<< " data points from "
		<< in_file
		<< " with the following fields: "
		<< std::endl;

	std::ofstream myFile(out_file.c_str(), std::ios::out | std::ios::binary);
	for (int j = 0; j < cloud->size(); j++) {

		myFile.write((char*)& cloud->at(j).x, sizeof(cloud->at(j).x));
		myFile.write((char*)& cloud->at(j).y, sizeof(cloud->at(j).y));
		myFile.write((char*)& cloud->at(j).z, sizeof(cloud->at(j).z));
		// myFile.write((char *)& cloud->at(j).intensity, sizeof(cloud->at(j).intensity)); // 正常intensity
		cloud->at(j).intensity = 0;
		myFile.write((char *)& cloud->at(j).intensity, sizeof(cloud->at(j).intensity)); // intensity = 0
		// myFile << cloud->at(j).x << " " << cloud->at(j).y << " " << cloud->at(j).z << std::endl;
		std::cout << "point: " << cloud->at(j).x << " " << cloud->at(j).y << " " << cloud->at(j).z << " " << cloud->at(j).intensity  << std::endl;
	}
	myFile.close();
}


int main(int argc, char **argv)
{
    std::string str1 =  argv[1] ;// "/home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.pcd";
    std::string str2 = argv[2] ;// "/home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.bin";
    convertPCDtoBin(str1,str2);

    return 0;
}