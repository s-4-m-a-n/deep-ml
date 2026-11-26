def mask_instruction_loss(batch, pad_token_id, ignore_index=-100):
    # Your code here
    L = max([len(item["tokens"]) for item in batch])

    inputs = []
    targets = []
    
    for item in batch:
        tokens = item["tokens"]
        instruction_length  = item["instruction_length"]

        padded = tokens + [pad_token_id]*(L -len(tokens))
    
        input_ = padded[:-1]
        target_ = padded[1:]

        seen = False
        for i in range(len(target_)):
            if i < instruction_length-1:
                target_[i] = ignore_index
            if target_[i] == pad_token_id:
                if not seen:
                    seen = True
                else:
                    target_[i] = ignore_index
    
        inputs.append(input_)
        targets.append(target_)
    return {"inputs": inputs, "targets": targets}
        

    
    
