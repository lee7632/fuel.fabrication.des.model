**Melter failure**
<br>A weibull distribution is used to simulate a general, random melter failure.
<br>'Weibull' is useful when there is not a lot of data available.
<br><br>Weibull distribution pdf: f(t) = (k/lambda)((t/lambda)^(k-1))exp(-(t/lambda)^k)
<br>Weibull distribution cdf: F(t) = 1 - exp(-(t/lambda)^k)
<br>
<br>With increasing time, F(t) approaches 1, so the probability of a failure increases; i.e, the equipment wears out.
<br><br>If the failure rate is constant over time, then k = 1.0.
<br>Then, 1/lambda = failure rate parameter.
<br>A 'rate parameter' is simply the reciprocal of the scale parameter (lambda).
<ul>
<li>operation_time is the 'real' time; i.e., the simulation ends when operation_time >= facility_operation.
<li>f(t) and F(t) are evaluated using failure_time.
<li>When a failure occurs, failure_time is reset.
<li>Reset of failure_time implies that a new equipment is installed with a 'new' failure distribution.
</ul>

<ul>
<b>Procedure</b>
<li>Melter process begins.
<li>After the melting process, a failure test is initiated.
<br>In reality, a halfway through the melter operation time, a failure test must be initiated.
<li>F(t = failure_time) is computed.
<li>A random number (n) between [0, 1) is generated from the uniform distribution.
<li>Failure occurs if n <= F(t).
<li>Therefore, if F(t) is close to 1; i.e., later in facility operation, it is more likely n <= F(t); i.e., more likely the equipment fails.
<li>If there is no failure, the operation continues. 
<li>If there is a failure, the maintenance loop starts.
</ul>
