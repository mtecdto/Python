let chavesView = document.querySelector("#chavesView");
let outputView = document.querySelector("#outputView");
let pvView = document.querySelector("#pvView");

/* PEDACOS DA STRING SQL */

const cmdSqlInicial = "INSERT INTO general_keys (idkey,keycontent,serialcontent,keystate,bancada,disco,memoria,pv) VALUES ";
const cmdSqlFinal = ";";
const shapeInicial = "(default,'";
const shapeFinal = `','',0,'',0,0,'`;
const shapeFinal2 = `')`;

let cmdSqlToCopy = "";

/*........*/

let shapeAux = "";

function concatenaShapeChave(vetorKeys,pv){
    let shapeConcatenado = null;

    for(let i=0; i < vetorKeys.length; i++){
        shapeConcatenado = `${shapeInicial}${vetorKeys[i]}${shapeFinal}${pv}${shapeFinal2}`;
        shapeAux = `${shapeAux}${shapeConcatenado},`;
    }
    
    shapeAux = shapeAux.substring(0,shapeAux.length - 1);
}

function inputParaVetorChaves(inputChaves){
    const chaves = inputChaves;
    const vetorChaves = chaves.split(" ");
    return vetorChaves
}

function generateBtn(){

    let chavesContent = chavesView.value;
    let pvContent = pvView.value;
    let vetKeys = inputParaVetorChaves(chavesContent);

    concatenaShapeChave(vetKeys,pvContent);

    const cmdSqlCompleto = `${cmdSqlInicial}${shapeAux}${cmdSqlFinal}`;
    cmdSqlToCopy = cmdSqlCompleto;
    outputView.innerText = `${cmdSqlCompleto}`;
}

async function clipboardCopyBtn(){

    await navigator.clipboard.writeText(cmdSqlToCopy);
    alert('Copiado para área de transferência');

}