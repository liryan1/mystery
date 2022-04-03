
// class Item {

//  private:
//   std::string description_;
//   std::optional<CalendarEvent> calendar_event_;
//   std::optional<Image> icon_;
//   ...
// };

class Item {
  virtual int Rank() const = 0;
  virtual void Rander(Display& display) const = 0;
};
 
class CalendarItem : public Item {
  int Rank() const override { return 0; }

};

class LinkItem : public Item {

};

class Todolist {
 public:

 private:
    std::vector<std::unique_ptr<Item>> items_;
};
