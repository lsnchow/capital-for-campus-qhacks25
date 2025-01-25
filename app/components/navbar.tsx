import React from 'react';

const Navbar: React.FC = () => {
    return (
        <nav>
            <ul className="flex flex-row space-x-4 p-4">
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;