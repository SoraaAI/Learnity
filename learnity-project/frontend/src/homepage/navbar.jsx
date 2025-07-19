function BrandName() {
    return (
        <>
            <h2 className="font-inter font-bold text-2xl  text-teal-300 bg-gradient-to-r from-emerald-200 to-cyan-200 bg-clip-text text-transparent">Learnity</h2>
        </>
    )
}

function NavLink() {
    const links = ["Home", "About", "Contact"]

    return (
        <ul className="flex items-center">
            {links.map((link, i) => 
            (<li key={i} className="flex ml-9 font-inter font-medium text-teal-200">{link}</li>))}
            <li className="ml-9 font-inter font-medium text-white bg-teal-300 px-2 py-1 rounded-3xl"><NavButton/></li>
        </ul>
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
            <nav className="p-4 flex justify-between">
                <BrandName />
                <NavLink/>
                {/* <NavButton/> */}
            </nav>
        </>
    )
}

export default Navbar