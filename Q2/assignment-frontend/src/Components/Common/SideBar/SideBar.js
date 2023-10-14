import {  Navbar, Image } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import "./SideBar.css";
import Logo from "../../../assets/images/logo.svg";
import Home from "../../../assets/images/home.svg";
import Schedule from "../../../assets/images/schedule.svg";


const SideBar = () => {
  const navigate = useNavigate();
  return (
    <>
      <div id="sidebar" className={`sideBar  sideBar `}>
        <div className="sideBarHeader">
          <Navbar.Brand
            className="logoWrap text-center d-block"
          >
            <Image
              src={Logo}
              alt="Cannabis One-Click"
              fluid
              className="MainLogo"
            />
          </Navbar.Brand>
          <ul className="navigation m-0">
            <li onClick={() => navigate("/")}>
              <a href="#">
              <Image src={Home} />
              <p className="m-0">Home</p>
              </a>
            </li>
            <li>
            <a href="#">
              <Image src={Schedule} />
              <p className="m-0" onClick={() => navigate("/schedule/post")}>Schedule</p>
              </a>
            </li>
          </ul>
        </div>
        {/* <MainNavigation hideSideBar={() => dispatch(setShrinkNavBar(false))} />
        <TransparentButton
          title="Logout"
          customClass={${styles.mobileLogoutBtn} py-3 px-2 gap-3 d-sm-none d-flex align-items-center}
          onClick={() => handleLogout()}
          href="#"
        >
          <i className="fi fi-br-sign-out-alt" />
        </TransparentButton> */}
      </div>
    </>
  );
};

export default SideBar;
