int c = 0;

// d is tied to c, c can be changed through d
auto& d = c;

// c can be changed but cannot be changed through e
const auto& e = c;
