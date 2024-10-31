import graphviz; graphviz.Source('''
digraph { 
    concentrate=True;
    rankdir=BT;
    node [shape=record];
    WE [label="Word embedding\n|{output:|input:}|{{m}|{V}}"];
    HL [label="MLP (Hidden layer weights)\n|{output:|input:}|{{h}|{m · (n-1)}}"];
    OL [label="Softmax (Output weights)\n|{output:|input:}|{{V}|{h + m · (n-1)}}"];
    WE -> HL
    HL -> OL
    WE -> OL
    node [shape=circle];
    wb [label=<W<sub>i-n-1</sub>>,fixedsize=true,width=0.7];
    wm [label="...",fixedsize=true,width=0.7];
    we [label=<W<sub>i-1</sub>>,fixedsize=true,width=0.7];
    wo  [label=<W<sub>i</sub>>,fixedsize=true,width=0.7];
    wb -> WE
    wm -> WE
    we -> WE
    OL  -> wo
}''').render(filename='MLPLM', format='svg');
