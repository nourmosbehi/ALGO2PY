document.addEventListener('DOMContentLoaded', function() {
    // Converter functionality
    const convertBtn = document.getElementById('convert-btn');
    const clearBtn = document.getElementById('clear-btn');
    const inputText = document.getElementById('input-text');
    const outputText = document.getElementById('output-text');
    const conversionType = document.getElementById('conversion-type');
    const exampleButtons = document.querySelectorAll('.example-buttons button');
    
    // Example data
    const examples = {
        'sorting-algo': {
            'algo_to_python': `Fonction tri_selection(tableau):
    Pour i de 0 à longueur(tableau) - 1 Faire
        min_index = i
        Pour j de i+1 à longueur(tableau) Faire
            Si tableau[j] < tableau[min_index] Alors
                min_index = j
        Fin Pour
        échanger(tableau, min_index, i)
    Fin Pour
Fin Fonction`,
            'python_to_algo': `def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]`
        },
        // More examples...
    };
    
    // Event listeners
    convertBtn.addEventListener('click', convert);
    clearBtn.addEventListener('click', clear);
    exampleButtons.forEach(btn => {
        btn.addEventListener('click', loadExample);
    });
    
    // Functions
    function convert() {
        const text = inputText.value.trim();
        if (!text) return;
        
        const type = conversionType.value;
        
        fetch('/converter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `input_text=${encodeURIComponent(text)}&conversion_type=${type}`
        })
        .then(response => response.json())
        .then(data => {
            outputText.textContent = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
            outputText.textContent = 'An error occurred during conversion.';
        });
    }
    
    function clear() {
        inputText.value = '';
        outputText.textContent = '';
    }
    
    function loadExample(e) {
        const exampleKey = e.target.dataset.example;
        const type = conversionType.value;
        
        if (examples[exampleKey] && examples[exampleKey][type]) {
            inputText.value = examples[exampleKey][type];
        }
    }
});