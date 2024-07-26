let playerScore = 0;
let compScore = 0;

let choices = document.querySelectorAll(".choice");
let msgOutput = document.querySelector("#msg")

let playerScoreMsg = document.querySelector("#user-score");
let compScoreMsg = document.querySelector("#comp-score");

const genCompChoice = () => {
    const options = ['rock','paper','sicssor']
    const choiceIdx = Math.floor(Math.random() * 3)
    return options[choiceIdx]
}

const win = (playerWin, playerChoice, compChoice) => {

    if (playerWin === true) {
        playerScore++;
        playerScoreMsg.innerText = playerScore;
        msg.innerText = `You win! Your ${playerChoice} beats ${compChoice}`;
        msg.style.backgroundColor = "green";
    }  else {
        compScore++;
        compScoreMsg.innerText = compScore;
        msg.innerText = `You Lost! Computer's ${compChoice} beats ${playerChoice} :(`;
        msg.style.backgroundColor = "red";
    }

};


const draw = () => {
    msg.innerText = `Its A Draw`;
    msg.style.backgroundColor = "gray";
}


const startGame = (playerChoice) => {

    const compChoice = genCompChoice()

    if (compChoice === playerChoice) {
        draw();
    }else {
        let playerWin = true
        if (playerChoice === 'rock') {
            playerWin = compChoice === 'paper' ? false:true;
        }else if (playerChoice === "paper"){
            playerWin = compChoice ==='scissor'? false:true;
        }else if (playerChoice === "scissor") {
            playerWin = compChoice === 'rock' ? false:true;
        }

        win(playerWin,playerChoice,compChoice);
    }

    if (playerScore >= 10 || compScore >= 10) {
        endGame(playerScore,compScore);
    }
}

const endGame = (playerScore,compScore) =>{
    if (playerScore < compScore){
        msg.innerText = `Game Over, You Lost by ${compScore - playerScore} 😭`;
        msg.style.backgroundColor = "red"
    }else if (compScore < playerScore) {
        msg.innerText = `Game Over, You Won by ${playerScore - compScore} 😁`;
        msg.style.backgroundColor = "green";
    }else if (compScore === playerScore) {
        msg.innerText = `Game Over, Its a Draw 😶`;
        msg.style.backgroundColor = "grey";
    }


}

choices.forEach((choice) => {
    choice.addEventListener("click", (event) => {
        startGame(choice.getAttribute("id"),)
    });
})
