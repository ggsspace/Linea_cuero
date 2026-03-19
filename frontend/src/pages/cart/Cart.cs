.cart-section {
  padding: 60px 50px;
  min-height: 80vh;
}

.cart-title {
  text-align: center;
  margin-bottom: 40px;
  font-size: 2.5rem;
  font-weight: 800;
  letter-spacing: -1px;
  color: white;
}

.cart-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  color: #cbd5e1;
  font-size: 1.2rem;
  margin-top: 80px;
}

.cart-items {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.cart-item {
  display: flex;
  align-items: center;
  gap: 20px;
  background-color: #1e293b;
  border: 1px solid #2d3748;
  border-radius: 16px;
  padding: 15px;
  transition: all 0.3s ease;
}

.cart-item:hover {
  border-color: #a855f7;
  box-shadow: 0 4px 15px rgba(168, 85, 247, 0.2);
}

.cart-item img {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 10px;
}

.cart-item-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.cart-item-info h3 {
  color: white;
  font-size: 1rem;
  font-weight: 700;
  margin: 0;
}

.cart-item-info span {
  font-size: 1rem;
  font-weight: 800;
  background: linear-gradient(135deg, #a855f7 0%, #7e22ce 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cart-item-quantity {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cart-item-quantity button {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: none;
  background: linear-gradient(135deg, #a855f7 0%, #7e22ce 100%);
  color: white;
  font-size: 1.1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.cart-item-quantity button:hover {
  filter: brightness(1.2);
  transform: scale(1.1);
}

.cart-item-quantity span {
  color: white;
  font-size: 1rem;
  font-weight: 700;
  min-width: 20px;
  text-align: center;
}

.cart-item-remove {
  background: transparent;
  border: 1px solid #ef4444;
  color: #ef4444;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cart-item-remove:hover {
  background: #ef4444;
  color: white;
}

.cart-summary {
  max-width: 800px;
  margin: 40px auto 0;
  background-color: #1e293b;
  border: 1px solid #2d3748;
  border-radius: 16px;
  padding: 25px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  color: white;
}

.cart-summary p {
  font-size: 1.1rem;
  margin: 0;
}

.cart-btn-primary {
  padding: 14px;
  font-size: 1rem;
  font-weight: 600;
  color: white;
  background: linear-gradient(135deg, #a855f7 0%, #7e22ce 100%);
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 10px 15px -3px rgba(168, 85, 247, 0.25);
}

.cart-btn-primary:hover {
  filter: brightness(1.15);
  transform: translateY(-2px);
}

.cart-btn-danger {
  padding: 14px;
  font-size: 1rem;
  font-weight: 600;
  color: #ef4444;
  background: transparent;
  border: 1px solid #ef4444;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.cart-btn-danger:hover {
  background: #ef4444;
  color: white;
}

@media (max-width: 768px) {
  .cart-section {
    padding: 40px 20px;
  }

  .cart-item {
    flex-wrap: wrap;
  }

  .cart-title {
    font-size: 1.8rem;
  }
}