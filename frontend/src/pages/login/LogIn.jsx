import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./LogIn.css";
// Importamos la imagen correctamente desde assets
import icon from "../../assets/login.png"; 

const LogIn = () => {
  const [role, setRole] = useState("usuario");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    console.log(`Iniciando sesión como ${role}:`, { email, password });
    navigate("/");
  };

  return (
    <div className="login-screen">
      <main className="login-main-container">
        {/* SECTOR IZQUIERDO: Selector de Rol */}
        <div className="role-selector-sidebar">
          <div 
            className={`role-option ${role === "usuario" ? "active" : ""}`}
            onClick={() => setRole("usuario")}
          >
            <div className="role-icon-bg">
              {/* Usamos la variable importada 'icon' */}
              <img src={icon} alt="Usuario" className="role-img" />
            </div>
            <span>Usuario</span>
          </div>

          <div 
            className={`role-option ${role === "vendedor" ? "active" : ""}`}
            onClick={() => setRole("vendedor")}
          >
            <div className="role-icon-bg">
              {/* CORRECCIÓN: También usamos 'icon' aquí en lugar de la ruta de texto */}
              <img src={icon} alt="Vendedor" className="role-img" />
            </div>
            <span>Vendedor</span>
          </div>
        </div>

        {/* SECTOR DERECHO: Formulario */}
        <div className="login-form-container">
          <form className="login-form-card" onSubmit={handleLogin}>
            <h2>Iniciar Sesión</h2>
            
            <div className="input-field">
              <input 
                type="email" 
                placeholder="Ingrese su correo" 
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required 
              />
            </div>

            <div className="input-field">
              <input 
                type="password" 
                placeholder="Ingrese su contraseña" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required 
              />
            </div>

            <button type="submit" className="btn-submit">Ingresar</button>
            
            <div className="form-footer">
              <p>¿No Tienes Cuenta? <Link to="/signup">Regístrate aquí</Link></p>
              <Link to="/recovery" className="forgot-password">¿Olvidaste tu Cuenta?</Link>
            </div>
          </form>
        </div>
      </main>
    </div>
  );
};

export default LogIn;