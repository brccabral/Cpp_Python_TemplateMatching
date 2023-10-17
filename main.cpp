#include <iostream>
#include <opencv4/opencv2/opencv.hpp>

int main(int argc, char const *argv[])
{
    cv::Mat farm_img = cv::imread("assets/farm.png", cv::IMREAD_UNCHANGED);
    cv::Mat needle_img = cv::imread("assets/needle.png", cv::IMREAD_UNCHANGED);

    // show farm
    cv::imshow("Farm", farm_img);
    cv::waitKey();
    cv::destroyAllWindows();

    // show needle
    cv::imshow("Needle", needle_img);
    cv::waitKey();
    cv::destroyAllWindows();

    cv::Mat result;
    result.create(farm_img.rows, farm_img.cols, CV_32FC1);
    cv::matchTemplate(farm_img, needle_img, result, cv::TM_CCOEFF_NORMED);

    // show result
    cv::imshow("Result", result);
    cv::waitKey();
    cv::destroyAllWindows();

    return 0;
}
