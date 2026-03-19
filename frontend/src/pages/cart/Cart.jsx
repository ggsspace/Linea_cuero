import "./Cart.css";
import { useCart } from "../../context/CartContext.jsx"; // Trae los datos y funciones del carrito
import { NavLink } from "react-router-dom";

const Cart = () => {
  const { cartItems, removeFromCart, updateQuantity, clearCart, totalItems, totalPrice } = useCart();

  return (
    <main>
      <section className="cart-section">
        <h2 className="cart-title">Tu Carrito</h2>

        {cartItems.length === 0 ? (
          <div className="cart-empty">
            <p>Tu carrito está vacío</p>
            <NavLink to="/productos">
              <button className="cart-btn-primary">Ver Productos</button>
            </NavLink>
          </div>
        ) : (
          <>
            <div className="cart-items">
              {cartItems.map((item) => (
                <div className="cart-item" key={item.id}>
                  <img src={item.image} alt={item.title} />
                  <div className="cart-item-info">
                    <h3>{item.title}</h3>
                    <span>{item.price}</span>
                  </div>
                  <div className="cart-item-quantity">
                    <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>-</button>
                    <span>{item.quantity}</span>
                    <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>
                  </div>
                  <button className="cart-item-remove" onClick={() => removeFromCart(item.id)}>✕</button>
                </div>
              ))}
            </div>

            <div className="cart-summary">
              <p>Total items: <strong>{totalItems}</strong></p>
              <p>Total: <strong>${totalPrice.toLocaleString()}</strong></p>
              <button className="cart-btn-danger" onClick={clearCart}>Vaciar carrito</button>
              <button className="cart-btn-primary">Finalizar compra</button>
            </div>
          </>
        )}
      </section>
    </main>
  );
};

export default Cart;