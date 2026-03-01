import { NavLink } from "react-router-dom";
import "./NavBar.css";
import senaLogo from "../../assets/logo_SENA.png";
import loginIcon from "../../assets/login.png";
import carritoIcon from "../../assets/carrito.png";

const NavBar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-logo">
          <img src={senaLogo} alt="SENA" className="logo-img" />
          <div className="logo-text">
            <span className="logo-title">SENA</span>
            <span className="logo-subtitle">CDMC</span>
          </div>
        </div>

        <ul className="navbar-links">
          <li><NavLink to="/" end>Inicio</NavLink></li>
          <li><NavLink to="/productos">Productos</NavLink></li>
          <li><NavLink to="/calendario">Calendario</NavLink></li>
          <li><NavLink to="/qa">Q&A</NavLink></li>
          <li><NavLink to="/cart">Carrito</NavLink></li>
        </ul>

        <div className="navbar-icons">
          <NavLink to="/login" className="icon-btn">
            <img src={loginIcon} alt="Login" className="nav-icon-img" />
          </NavLink>
          <div className="icon-btn">
            <img src={carritoIcon} alt="Carrito" className="nav-icon-img" />
          </div>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;