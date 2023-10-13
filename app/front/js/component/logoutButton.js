import React, { useEffect, useState, useContext } from "react"
import { useNavigate } from 'react-router-dom';
import { Context } from "../store/appContext"

const LogoutButton = () => {
  const navigate = useNavigate();
  const { store, actions } = useContext(Context)

  const handleLogout = () => {
    actions.logoutUser()
    navigate('/login'); 
  }

  return (
    <div className="me-2">
    <button className="btn btn-warning" onClick={handleLogout}>
      Logout
    </button>
    </div>
  );
}

export default LogoutButton;