cmake_minimum_required(VERSION 3.10)

project(MasterMatcherVST)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add source files
set(SOURCES
    PluginProcessor.h
    PluginProcessor.cpp
    PluginEditor.h
    PluginEditor.cpp
)

# Create library target
add_library(${PROJECT_NAME} SHARED ${SOURCES})

# Set include directories
include_directories(
    "${JUCE_PATH}/modules"
)

# Set output directories
set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
)

# Add plugin formats
if(WIN32)
    add_definitions(-DJUCE_PLUGINHOST_VST3=1)
    add_definitions(-DJUCE_PLUGINHOST_AAX=1)
endif()

# Add JUCE configuration
add_definitions(
    -DJUCE_STANDALONE_PLUGIN=1
    -DJUCE_PLUGINHOST_AU=1
    -DJUCE_PLUGINHOST_VST=1
    -DJUCE_PLUGINHOST_VST3=1
    -DJUCE_PLUGINHOST_AAX=1
)
