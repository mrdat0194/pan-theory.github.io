from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def first():
    # Defining the network structure

    model = BayesianModel([('A', 'T1'), ('A', 'T2')])
    # Defining the CPDs:

    cpd_t1 = TabularCPD('T1', 2, [[0.9, 0.05],
                                  [0.1, 0.95]],
                        evidence=['A'], evidence_card=[2])
    cpd_t2 = TabularCPD('T2', 2, [[0.8, 0.1],
                                  [0.2, 0.9]],
                        evidence=['A'], evidence_card=[2])

    cpd_d = TabularCPD('A', 2, [[1/3], [2/3]])


    # Associating the CPDs with the network structure.
    model.add_cpds(cpd_t1, cpd_t2 , cpd_d)

    # Some other methods
    print(model.get_cpds())

    print(model.check_model())

    # VariableElimination
    infer = VariableElimination(model)

    # 1. A vs B which has more chance to get when one T1 or T2 positive

    posterior_p = infer.query(['T1','T2'], evidence={'A': 0})
    Pa = posterior_p.values[0][1]+ posterior_p.values[1][0]

    posterior_p = infer.query(['T1','T2'], evidence={'A': 1})
    Pb = posterior_p.values[0][1]+ posterior_p.values[1][0]

    posterior_p = infer.query(['A'])

    Pt = Pb*posterior_p.values[0] + Pa*posterior_p.values[1]

    print(Pa*posterior_p.values[1]/Pt)
    print(26/33)

    # 2. 2 T are positive, A chance to get?

    posterior_p = infer.query(['T1','T2'], evidence={'A': 0})
    Pa = posterior_p.values[0][0]

    posterior_p = infer.query(['T1','T2'], evidence={'A': 1})
    Pb = posterior_p.values[0][0]

    posterior_p = infer.query(['A'])

    Pt = Pb*posterior_p.values[0] + Pa*posterior_p.values[1]

    print(Pa*posterior_p.values[1]/Pt)
    print(((2/3)*(18/25))/(289/600))

if __name__ == '__main__':
    first()
