document.addEventListener('DOMContentLoaded', () => {
    const pegs = {
        'peg-1': [],
        'peg-2': [],
        'peg-3': []
    };
    const diskCount = 5;
    const pegElements = {
        'peg-1': document.getElementById('peg-1'),
        'peg-2': document.getElementById('peg-2'),
        'peg-3': document.getElementById('peg-3')
    };
    let selectedDisk = null;
    let selectedPegId = null;

    function initGame() {
        // Initialize the first peg with disks in descending order of size
        for (let i = diskCount; i >= 1; i--) {
            pegs['peg-1'].push(i);
        }
        render();
    }

    function render() {
        // Clear all pegs
        Object.values(pegElements).forEach(peg => peg.innerHTML = '');

        // Render disks on each peg
        for (const [pegId, disks] of Object.entries(pegs)) {
            const pegElement = pegElements[pegId];
            disks.forEach(diskSize => {
                const diskElement = document.createElement('div');
                diskElement.classList.add('disk');
                diskElement.style.width = `${diskSize * 30 + 40}px`;
                diskElement.style.backgroundColor = `hsl(${diskSize * 40}, 70%, 50%)`;
                diskElement.innerText = diskSize;
                diskElement.dataset.size = diskSize;
                
                diskElement.addEventListener('click', (e) => handleDiskClick(pegId, diskSize));
                pegElement.appendChild(diskElement);
            });
        }
    }

    function handleDiskClick(pegId, diskSize) {
        const disksOnPeg = pegs[pegId];
        const topDisk = disksOnPeg[disksOnPeg.length - 1];

        // Only the top disk of a peg can be selected
        if (diskSize !== topDisk) {
            alert('You can only move the top disk!');
            return;
        }

        if (!selectedDisk) {
            // Select the disk
            selectedDisk = diskSize;
            selectedPegId = pegId;
            highlightPeg(pegId, true);
        } else {
            // Try to move the selected disk to the clicked peg
            if (selectedPegId === pegId) {
                // Deselect if clicking the same peg
                selectedDisk = null;
                selectedPegId = null;
                highlightPeg(pegId, false);
            } else {
                moveDisk(selectedPegId, pegId);
            }
        }
    }

    function highlightPeg(pegId, isHighlighted) {
        pegElements[pegId].style.backgroundColor = isHighlighted ? 'rgba(255, 255, 0, 0.2)' : '';
    }

    function moveDisk(fromPegId, toPegId) {
        const fromPeg = pegs[fromPegId];
        const toPeg = pegs[toPegId];
        const diskToMove = fromPeg[fromPeg.length - 1];
        const topDiskOnTarget = toPeg[toPeg.length - 1];

        // Rule: Cannot place a larger disk on top of a smaller disk
        if (topDiskOnTarget && diskToMove > topDiskOnTarget) {
            alert('Invalid move: Cannot place a larger disk on top of a smaller one!');
            selectedDisk = null;
            selectedPegId = null;
            highlightPeg(fromPegId, false);
            return;
        }

        // Perform the move
        fromPeg.pop();
        toPeg.push(diskToMove);

        // Reset selection
        selectedDisk = null;
        selectedPegId = null;
        highlightPeg(fromPegId, false);

        render();
        checkWin();
    }

    function checkWin() {
        // Win condition: All disks are on the third peg
        if (pegs['peg-3'].length === diskCount) {
            setTimeout(() => {
                alert('Congratulations! You solved the Tower of Hanoi!');
                initGame(); // Reset game
            }, 100);
        }
    }

    // Allow clicking on an empty peg to move a selected disk there
    Object.entries(pegElements).forEach(([pegId, element]) => {
        element.addEventListener('click', (e) => {
            // Only handle click if the target is the peg itself, not a disk
            if (e.target === element) {
                if (selectedDisk) {
                    moveDisk(selectedPegId, pegId);
                }
            }
        });
    });

    initGame();
});
