function BrandName() {
    return (
        <>
            <h2 className="BrandName-navbar">Learnity</h2>
        </>
    )
}

function NavLink() {
    return(
        <>
            <ul className="NavLink-navbar">
                <li className="navlink">
                    <a href="#">Home</a>
                </li>
                <li className="navlink">
                    <a href="#">About</a>
                </li>
                <li className="navlink">
                    <a href="#">Contact</a>
                </li>
                <li>
                    <NavButton/>
                </li>
            </ul>
        </>
    )
}

function NavButton() {
    return (
        <>
            <a href="#">
                <button className="NavButton-navbar" id="button-navbar">
                    Join With Us!
                </button>
            </a>
        </>
    )
}

function Navbar() {
    return (
        <>
            <nav>
                <BrandName/>
                <NavLink/>
                {/* <NavButton/> */}
            </nav>
        </>
    )
}

export default Navbar