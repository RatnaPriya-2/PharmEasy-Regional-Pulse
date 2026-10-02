# ==============================================================================
# Task 3.1 — CII Insight Generator (draft_report_v1)
# ==============================================================================

from metrics_engine import flagged_regions, monthly_summary

# Task 3.1: CII insight generator
def draft_report_v1(flagged_regions, metrics):
    cii = {}

    for region, changes in flagged_regions.items():

        insight = ""

        sales_april = metrics[region]['2026-04']
        sales_may = metrics[region]['2026-05']
        sales_june = metrics[region]['2026-06']

        if len(changes) == 2:

            if changes['apr_to_may'] > 0:
                direction1 = "increased"
            else:
                direction1 = "decreased"

            if changes['may_to_jun'] > 0:
                direction2 = "increased"
            else:
                direction2 = "decreased"

            insight = f"{region}'s sales {direction1} by {abs(changes['apr_to_may'])}% from April to May, changing from ₹{sales_april:.2f} to ₹{sales_may:.2f}. Sales then {direction2} by {abs(changes['may_to_jun'])}% from May to June, changing to ₹{sales_june:.2f}."

        elif len(changes) == 1:

            if 'apr_to_may' in changes:

                if changes['apr_to_may'] > 0:
                    direction = "increased"
                else:
                    direction = "decreased"

                insight = f"{region}'s sales {direction} by {abs(changes['apr_to_may'])}% from April to May, changing from ₹{sales_april:.2f} to ₹{sales_may:.2f}."

            elif 'may_to_jun' in changes:

                if changes['may_to_jun'] > 0:
                    direction = "increased"
                else:
                    direction = "decreased"

                insight = f"{region}'s sales {direction} by {abs(changes['may_to_jun'])}% from May to June, changing from ₹{sales_may:.2f} to ₹{sales_june:.2f}."

        template = f"""Context:
We examined {region}'s sales performance across April, May and June 2026
to identify significant month-on-month changes.

Insight:
{insight}

Implication:
This significant movement in {region}'s sales should be reviewed to understand
the factors contributing to the change and determine the appropriate next check."""

        cii[region] = template

    return cii

if __name__ == "__main__":
    drafts = draft_report_v1(flagged_regions, monthly_summary)
    print("Generated Draft Reports (CII Blocks):")
    for region, block in drafts.items():
        print(f"\n--- {region} ---")
        print(block)
