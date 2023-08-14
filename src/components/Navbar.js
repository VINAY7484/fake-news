import React from 'react';
import './Navbar.css'


const Navbar = () => {
  return (
    <div className='glass'>
       <nav className="navbar">
      <span className="navbar-badge">20+</span>
      <div className="navbar-end">
        {/* <img className="navbar-logo" src="logo.svg" /> */}
        <button className="icon-button">
          <i className="uil uil-search"></i>
        </button>
      </div>
      <div className="navbar-center">
        <button className="active">
          <i className="uil uil-estate"></i>
        </button>
        <button>
          <i className="uil uil-play-circle"></i>
        </button>
        <button>
          <i className="uil uil-store"></i>
        </button>
        <button>
          <i className="uil uil-users-alt"></i>
        </button>
        <button>
          <i className="uil uil-bars"></i>
        </button>
      </div>
      <div className="navbar-end">
        <button className="icon-button">
          <i className="uil uil-plus"></i>
        </button>
        <button className="icon-button">
          <i className="uil uil-facebook-messenger-alt"></i>
        </button>
        <button className="icon-button">
          <i className="uil uil-bell"></i>
        </button>
        {/* <img className="navbar-avatar" src="avatar.png" /> */}
      </div>
    </nav>
    </div>
  );
};

export default Navbar;