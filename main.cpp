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

    double minVal;
    double maxVal;
    cv::Point minLoc;
    cv::Point maxLoc;
    minMaxLoc(result, &minVal, &maxVal, &minLoc, &maxLoc, cv::Mat());

    int width = needle_img.cols;
    int height = needle_img.rows;

    cv::rectangle(farm_img, maxLoc, cv::Point(maxLoc.x + width, maxLoc.y + height), cv::Scalar(0, 255, 255), 2);

    // show farm
    cv::imshow("Farm", farm_img);
    cv::waitKey();
    cv::destroyAllWindows();


    return 0;
}
