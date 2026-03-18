import { BrowserRouter, Routes, Route } from "react-router-dom";

import NavBar from "./components/navbar/NavBar.jsx";
import Home from "./pages/home/Home.jsx";
import Products from "./pages/products/Products.jsx"; 
import Calendar from "./pages/calendar/Calendar.jsx";
import QA from "./pages/qa/QA.jsx";
import LogIn from "./pages/login/LogIn.jsx";
import Cart from "./components/cart/Cart.jsx";
import SignUp from "./pages/signup/SignUp.jsx";
import Events from "./pages/events/Events.jsx";


function App() {
  return (
    <BrowserRouter>
      <NavBar />
      
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
        <Route path="/calendario" element={<Calendar />} />
        <Route path="/qa" element={<QA />} />
        <Route path="/login" element={<LogIn />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/events" element={<Events />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
