import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./LogIn.css";

const LogIn = () => {

  const [role, setRole] = useState("usuario"); // Estado para alternar rol
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    console.log('Iniciando como ${role}:', { email, password });
    // Aquí iría tu lógica de Firebase o Backend
    navigate("/");
  };

  return (
    <main>
      <section >
          <div className="login-container">
          

          <main className="login-main-container">
            {/* Lado Izquierdo: Selector de Rol */}
            <div className="role-selector-container">
              <div 
                className={`role-option ${role === "usuario" ? "active" : ""}`}
                onClick={() => setRole("usuario")}
              >
                <div className="role-icon">👤</div>
                <span>Usuario</span>
              </div>
              <div 
                className={`role-option ${role === "vendedor" ? "active" : ""}`}
                onClick={() => setRole("vendedor")}
              >
                <div className="role-icon">👤</div>
                <span>Vendedor</span>
              </div>
            </div>

            {/* Lado Derecho: Formulario */}
            <div className="login-card">
              <form className="login-form-box" onSubmit={handleLogin}>
                <h2>Iniciar Sesión</h2>
                <div className="input-group">
                  <input 
                    type="email" 
                    placeholder="Ingrese su correo" 
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required 
                  />
                </div>
                <div className="input-group">
                  <input 
                    type="password" 
                    placeholder="Ingrese su contraseña" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required 
                  />
                </div>
                <button type="submit" className="btn-ingresar">Ingresar</button>
                
                <div className="login-footer-links">
                  <p>¿No Tienes Cuenta? <Link to="/signup">Regístrate aquí</Link></p>
                  <Link to="/recovery" className="forgot-link">¿Olvidaste tu Cuenta?</Link>
                </div>
              </form>
            </div>
          </main>
        </div>
      </section>

    </main>
  );
};
export default LogIn;

