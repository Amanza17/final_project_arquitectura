cmake_minimum_required(VERSION 3.8)
project(depth_worker)

# Opciones de compilación
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encuentra dependencias
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(vision_msgs REQUIRED)
find_package(image_transport REQUIRED)
find_package(tf2_sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(message_filters REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(pcl_ros REQUIRED)
find_package(image_geometry REQUIRED)
find_package(depth_image_proc REQUIRED)
find_package(yolo_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

find_package(OpenCV REQUIRED)

set(dependencies
  rclcpp
  sensor_msgs
  tf2_sensor_msgs
  vision_msgs
  image_transport
  cv_bridge
  OpenCV
  message_filters
  pcl_conversions
  pcl_ros
  image_geometry
  depth_image_proc
  yolo_msgs
  geometry_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs

)

include_directories(include)

# Crea la librería
add_library(${PROJECT_NAME} SHARED
  src/depth_worker/YoloDetectionNode.cpp
  src/depth_worker/YoloParserNode.cpp
  src/depth_worker/DetectionTo3DfromPCNode.cpp
)
ament_target_dependencies(${PROJECT_NAME} ${dependencies})


# Ejecutables
add_executable(yolo_detection src/yolo_detection_main.cpp)
ament_target_dependencies(yolo_detection ${dependencies})
target_link_libraries(yolo_detection ${PROJECT_NAME})

add_executable(yolo_parser src/yolo_parser.cpp)
ament_target_dependencies(yolo_parser ${dependencies})
target_link_libraries(yolo_parser ${PROJECT_NAME})

add_executable(detection_2d_to_3d_pc2 src/detection_2d_to_3d_pc2_main.cpp)
ament_target_dependencies(detection_2d_to_3d_pc2 ${dependencies})
target_link_libraries(detection_2d_to_3d_pc2 ${PROJECT_NAME})

# Instalación
install(TARGETS
  ${PROJECT_NAME}
  yolo_detection
  yolo_parser
  detection_2d_to_3d_pc2
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch config DESTINATION share/${PROJECT_NAME})

# Testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)

  ament_lint_auto_find_test_dependencies()
endif()

# Exportaciones
ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})
ament_export_dependencies(${dependencies})

ament_package()
