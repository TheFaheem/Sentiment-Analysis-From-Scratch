from torchinfo import summary
from prettytable import PrettyTable

# Print a Comprehensive Summary of the Model, Modules, Submodules, Parameter Counts
def model_summary(model, generator)
review_batch, label, mask_batch = next(generator)
print(summary(model, input_data=[review_batch.to("cuda:0"), mask_batch.to("cuda:0")]))


# Utility function to print the Modules, SubModules and their Corresponding trainable parmeters in a Clean Table Structure
def count_parameters(model):
    table = PrettyTable(["Modules", "Parameters"])
    total_params = 0
    for name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue
        params = parameter.numel()
        table.add_row([name, params])
        total_params += params
    print(table)
    print(f"Total Trainable Params: {total_params}")
    return total_params
