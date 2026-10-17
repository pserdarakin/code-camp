import { useEffect, useState } from "react";
import "./App.css";

// Start a React and TypeScript project with Vite.
// Fetch users from jsonplaceholder.typicode.com/users and
// show their names in a list.
// If a type blocks you, use any for now and keep going.

// How to fetch/intake data from json from another resource/web link into
// I ll need fetch the id with their names from the API source, => useState and useEffect check from docs
// and hold that users inside the app,
// which fields should I show?
//

const url = "https://jsonplaceholder.typicode.com/users";

function App() {
  // I have initiliazed the states/hold here with example values
  const [users, setUsers] = useState<any[]>([]);
  const [error, setError] = useState(null);

  // its because useEffect hooks are connects external source i ll use this to fetch data, so now ill check the documentation
  useEffect(() => {
    async function loadUsers() {
      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`Response status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
      } catch (error) {
        console.error(error);
      }
    }
    loadUsers();
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
