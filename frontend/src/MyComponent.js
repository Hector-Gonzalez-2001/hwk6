/**
 * @file: MyComponent.js
 * @author: Jared McArthur
 * @description: This is a button that you can toggle on and off. Very stupid code.
 * @returns: MyComponent
 */

// It assumes the Flask app is running on port 5000
// By default, the React app runs on 3000 and the Flask app runs on 5000

import React, { useState } from "react";
import { Button, TextField } from '@material-ui/core';

export default function MyComponent() {
    const [toggleButton, setButton] = useState("");
    const [toggleOutput, setOutput] = useState("");

    return (
        <div>
            <p>This is a button that you can toggle on and off</p>
            <TextField
                onChange={(e) => setButton(e.target.value)} />
            <Button
                variant="outlined"
                onClick={() => {
                    fetch("http://127.0.0.1:5000/toggle_button/" + toggleButton)
                        .then(response =>
                            response.json()
                        )
                        .then(data => {
                            setButton(data.button)
                            setOutput(data.button)
                        })
                        .catch(error => {
                            console.log(error)
                        })
                }}
            >
                Submit!
            </Button>

            <h1>
                {toggleOutput}
            </h1>

        </div>
    );
}