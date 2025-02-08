return function sanitizeInput(input) {
      let s= ""
      for (let i=0; i<input.length; i++) {
            if (input[i]=="@"||input[i]=="#"||input[i]=="$"||input[i]=="%"||input[i]=="&"||input[i]=="*"||input[i]=="!"||input[i]=="<"||input[i]==">"||input[i]=="?") {
                  s+="_"
            } else {
                  s+=input[i]
            }
      }
      return s
}
