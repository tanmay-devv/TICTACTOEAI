cmake_minimum_required(VERSION 3.10)
project(TTT-project)
find_package(X11)
add_executable(TTT main.cpp)

target_link_libraries(TTT
        ${X11_LIBRARIES}
        )                                                  
