// Copyright 2023 Intelligent Robotics Lab
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef depth_worker__YOLODETECTIONNODE_HPP_
#define depth_worker__YOLODETECTIONNODE_HPP_

#include <memory>

#include "yolo_msgs/msg/detection_array.hpp"
#include "vision_msgs/msg/detection2_d_array.hpp"

#include "rclcpp/rclcpp.hpp"

namespace depth_worker
{

class YoloDetectionNode : public rclcpp::Node
{
public:
  YoloDetectionNode();

private:
  void detection_callback(const yolo_msgs::msg::DetectionArray::ConstSharedPtr & msg);

  rclcpp::Subscription<yolo_msgs::msg::DetectionArray>::SharedPtr detection_sub_;
  rclcpp::Publisher<vision_msgs::msg::Detection2DArray>::SharedPtr detection_pub_;
};

}  // namespace camera

#endif  // depth_worker__YOLODETECTIONNODE_HPP_
