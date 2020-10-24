import 'package:uuid/uuid.dart';

enum Status { undone, done }

class HabitStroke {
  String id;
  String name;
  int color;
  int order;
  final int createdAt;

  HabitStroke(this.name, this.order)
      : id = Uuid().v4(),
        color = 0xFF26A69A,
        createdAt = new DateTime.now().toUtc().millisecondsSinceEpoch;
}

class Habit {
  String strokeId;
  Status status = Status.undone;
  String date;
  int doneAt;

  Habit(this.strokeId, this.date);

  done() {
    this.status = Status.done;
    this.doneAt = new DateTime.now().toUtc().millisecondsSinceEpoch;
  }

  undone() {
    this.status = Status.undone;
  }
}
