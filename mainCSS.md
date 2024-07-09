  <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: Arial, sans-serif;
            overflow: hidden;
            background-color: #000000;
        }
        .snow {
            color: white;
            position: absolute;
            animation: fall linear;
            opacity: 0.7;
            font-family: monospace;
            font-size: 20px;
        }
        @keyframes fall {
            to {
                transform: translateY(100vh);
            }
        }
        .container {
            position: relative;
            z-index: 1;
            background-color: rgba(26, 26, 26, 0.7);
            border-radius: 50px;
            box-shadow: 20px 20px 60px #000000, -20px -20px 60px #333333;
            padding: 50px;
            text-align: center;
            max-width: 80%;
            margin: 5px auto;
        }
        h1 {
            color: #ffffff;
            margin-bottom: 20px;
            font-size: 24px;
        }
        .name {
            color: #ff0000;
        }
        .social-icons {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .icon {
            width: 40px;
            height: 40px;
            margin: 0 10px;
            background-color: rgba(26, 26, 26, 0.7);
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 5px 5px 15px #000000, -5px -5px 15px #333333;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #ffffff;
            text-decoration: none;
        }
        .icon:hover {
            box-shadow: inset 5px 5px 10px #000000, inset -5px -5px 10px #333333;
        }
        #txt-rotate {
            min-height: 1.2em;
            display: inline-block;
        }
        .wrap {
            border-right: 0.08em solid #fff;
            padding-right: 5px;
        }
        #snow-pile {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50px;
            display: flex;
            flex-wrap: wrap;
            align-items: flex-end;
            overflow: hidden;
        }
    </style>