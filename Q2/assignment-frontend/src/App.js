import { BrowserRouter, Route, Routes } from "react-router-dom";
import SideBar from "./Components/Common/SideBar/SideBar";
import { Dashboard } from "./Components/Dashboard/Dashboard";
import { Header } from "./Components/Common/Header/Header";
import { ScheduledPosts } from "./Components/ScheduledPosts.js/ScheduledPosts";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <SideBar />
      <Header />
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/schedule/post" element={<ScheduledPosts />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
