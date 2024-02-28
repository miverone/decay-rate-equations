import ipywidgets as widgets
from ipywidgets import interact, interactive, interactive_output
from ipywidgets import Layout, Button, Box, VBox, HBox
from plot_asymmetries import plot_asymmetries
from declare_dec import dm, dg, gs, r, delta, gamma, beta, k
from declare_acc import a_acc, n_acc, b_acc, beta_acc, cutoff_acc
from declare_res import sigma_t
from declare_ft import omega, d_omega, eff, d_eff

# asymmetries
a_prod=widgets.BoundedFloatText(value=-0.01, min=-1, max=1, step=0.001, continuous_update=False, description=r'$a_{prod}$',layout=widgets.Layout(width='200px'))
a_det=widgets.BoundedFloatText(value=0.01, min=-1, max=1, step=0.001, continuous_update=False, description=r'$a_{det}$',layout=widgets.Layout(width='200px'))
# plotting
xmin=widgets.BoundedFloatText(value=0, min=0, max=100, step=1, continuous_update=False, description=r'$t_{min}$ [ps]',layout=widgets.Layout(width='200px'))
xmax=widgets.BoundedFloatText(value=5, min=0, max=100, step=1, continuous_update=False, description=r'$t_{max}$ [ps]',layout=widgets.Layout(width='200px'))
y_tag=widgets.BoundedFloatText(value=0.4, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{tag}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_untag=widgets.BoundedFloatText(value=0.2, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{untag}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_mix=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{mix}$ [a.u.]',layout=widgets.Layout(width='200px'))
name=widgets.Text(value='plots/asymmetries.eps',continuous_update=False,layout=widgets.Layout(width='200px'))
save=widgets.ToggleButton(value=False,description='Save',layout=widgets.Layout(width='200px'))
# select
b_f = widgets.Checkbox(value=True,description=r'$B$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_f = widgets.Checkbox(value=True,description=r'$\overline{B}$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_fbar = widgets.Checkbox(value=True,description=r'$\overline{B}$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
b_fbar = widgets.Checkbox(value=True,description=r'$B$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
fold_amix = widgets.Checkbox(value=True,description=r'fold $A_{mix}$',disabled=False,layout=widgets.Layout(width='200px'))
k_acc= widgets.Checkbox(value=True,description=r'Acceptance',disabled=False,layout=widgets.Layout(width='200px'))
k_res= widgets.Checkbox(value=True,description=r'Resolution',disabled=False,layout=widgets.Layout(width='200px'))
k_tag= widgets.Checkbox(value=True,description=r'Tagging',disabled=False,layout=widgets.Layout(width='200px'))

## Asymmetries
wbox_asymm = HBox([VBox([a_prod,a_det]),
                   VBox([xmin,xmax,y_tag,y_untag,y_mix]),
                   VBox([k_acc,k_res,k_tag,fold_amix]),
                   VBox([b_f,bbar_f,bbar_fbar,b_fbar]),
                   VBox([name,save])])
asymm_pars = interactive_output(plot_asymmetries,{'a_prod':a_prod,'a_det':a_det,
                                            'omega':omega,'d_omega':d_omega,'eff':eff,'d_eff':d_eff,
                                            'sigma_t':sigma_t,
                                            'a_acc':a_acc,'n_acc':n_acc,'b_acc':b_acc,'beta_acc':beta_acc,'cutoff_acc':cutoff_acc,
                                            'dm':dm,'dg':dg,'gs':gs,
                                            'r':r,'delta':delta,'gamma':gamma,'beta':beta,'k':k,
                                            'xmin':xmin,'xmax':xmax,'y_tag':y_tag,'y_untag':y_untag,'y_mix':y_mix,
                                            'name':name,'save':save,
                                            'k_acc':k_acc,'k_res':k_res,'k_tag':k_tag,
                                            'b_f':b_f,
                                            'bbar_f':bbar_f,
                                            'bbar_fbar':bbar_fbar,
                                            'b_fbar':b_fbar,
                                            'fold_amix':fold_amix})
