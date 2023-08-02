// Design a chess game

// abstract class
class Piece {
    int x;
    int y;
    void move_to(int new_x, int new_y) {
        x = new_x;
        y = new_y;
    }
};

// composition example
class Bishop2 {
    // now piece does not directly access the parent function
    Piece piece;
    void move_to(int new_x, int new_y) {
        piece.move_to(new_x, new_y);
    }
};

// inheritance example
class Bishop : public Piece {
    bool isvalid();
    void move_to(int new_x, int new_y) {
        // problem: breaks encapsulation
        // parent function cannot know what the child class needs
        // leaky abstraction
        if (isvalid)
            Piece::move_to(new_x, new_y);
    }
};

class Board {};
