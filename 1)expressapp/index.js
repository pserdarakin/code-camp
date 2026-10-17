import express from "express";

const app = express();
const port = 3000;

app.use(express.json()); // So that body gets read as json

app.get("/", (req, res) => {
  res.send("Hello World!");
});

// I am building a POST/tasks, it takes a title and a due date, and saves the task.
// good output -> 201
// what goes wrong? missing title, no due date, not to save the task, bad date format
// error messages i would expect no title given, title is required message.
//
app.post("/tasks", (req, res) => {
  res.status(201).json(req.body);
});
// curl -X POST http://localhost:3000/tasks -H "Content-Type: application/json" -d '{"title": "Buy milk", "due_date": "2026-10-10"}'

app.listen(port, () => {
  console.log(`Server running on port ${port}.`);
});
