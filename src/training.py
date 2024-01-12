from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from json_reader import result_dict
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

train_data = [f"{prompt} {response}" for prompt, response in result_dict.items()]
tokenized_datasets = TextDataset(
    tokenizer=tokenizer,
    file_path="dummy_file", 
    block_size=128,
    overwrite_cache=True,
    train_data=train_data,
)
training_args = TrainingArguments(
    output_dir="./output",
    overwrite_output_dir=True,
    num_train_epochs=10,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)
training_args.device = "cpu"
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    train_dataset=tokenized_datasets,
)

trainer.train()
