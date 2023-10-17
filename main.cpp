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

    // reset farm
    farm_img = cv::imread("assets/farm.png", cv::IMREAD_UNCHANGED);

    float threshold = 0.6f;
    cv::Mat result_threshold = result >= threshold;
    std::vector<cv::Point> loc;

    for (int row = 0; row < result_threshold.rows; row++)
    {
        for (int col = 0; col < result_threshold.cols; col++)
        {
            if (result_threshold.at<bool>(row, col))
            {
                loc.emplace_back(col, row);
            }
        }
    }

    std::cout << loc.size() << std::endl;

    for (auto &&p : loc)
    {
        cv::rectangle(farm_img, p, cv::Point(p.x + width, p.y + height), cv::Scalar(0, 255, 255), 2);
    }

    // show farm
    cv::imshow("Farm", farm_img);
    cv::waitKey();
    cv::destroyAllWindows();

    std::vector<cv::Rect> rectangles;
    for (auto &&p : loc)
    {
        rectangles.emplace_back(p.x, p.y, width, height);
        // force a duplication so cv::groupRectangles don't remove
        // locations that have only one rectangle
        rectangles.emplace_back(p.x, p.y, width, height);
    }
    cv::groupRectangles(rectangles, 1, 0.2);

    std::cout << rectangles.size() << std::endl;

    // reset farm
    farm_img = cv::imread("assets/farm.png", cv::IMREAD_UNCHANGED);

    // loop the new rectangles
    for (auto &&r : rectangles)
    {
        cv::rectangle(farm_img, r, cv::Scalar(0, 255, 255), 2);
    }

    // show farm
    cv::imshow("Farm", farm_img);
    cv::waitKey();
    cv::destroyAllWindows();

    return 0;
}
