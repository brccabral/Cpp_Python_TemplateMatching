#include <iostream>
#include <opencv4/opencv2/opencv.hpp>

int main(int argc, char const *argv[])
{
    cv::Mat farm_img = cv::imread("assets/farm.png", cv::IMREAD_UNCHANGED);
    cv::Mat needle_img = cv::imread("assets/needle.png", cv::IMREAD_UNCHANGED);

    cv::imshow("Farm", farm_img);
    cv::waitKey();
    cv::destroyAllWindows();

    return 0;
}
