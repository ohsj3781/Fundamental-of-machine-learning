CXX = g++
SRC = problem02.cpp
OBJ = $(SRC:.cpp=.o)
TARGET = program

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) -o $(TARGET) $(OBJ)

%.o: %.cpp
	$(CXX) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJ)
